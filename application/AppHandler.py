import psutil
from subprocess import PIPE
from datetime import datetime
import pandas as pd
import time
import os
import argparse

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

class AppHandler:
    """
    A class which works as a task manager.
    Based on https://www.thepythoncode.com/article/make-process-monitor-python
    """
    def __init__(self):
        self.__processes = []

    def get_processes_info(self):
        # the list the contain all process dictionaries
        processes = []
        for process in psutil.process_iter():
            # get all process info in one shot
            with process.oneshot():
                # get the process id
                pid = process.pid
                if pid == 0:
                    # System Idle Process for Windows NT, useless to see anyways
                    continue
                # get the name of the file executed
                name = process.name()
    
                # get the time the process was spawned
                try:
                    create_time = datetime.fromtimestamp(process.create_time())
                except OSError:
                    # system processes, using boot time instead
                    create_time = datetime.fromtimestamp(psutil.boot_time())
                
                try:
                    # get the number of CPU cores that can execute this process
                    cores = len(process.cpu_affinity())
                except psutil.AccessDenied:
                    cores = 0
                # get the CPU usage percentage
                cpu_usage = process.cpu_percent()

                # get the status of the process (running, idle, etc.)
                status = process.status()

                try:
                    # get the process priority (a lower value means a more prioritized process)
                    nice = int(process.nice())
                except psutil.AccessDenied:
                    nice = 0

                try:
                    # get the memory usage in bytes
                    memory_usage = process.memory_full_info().uss
                except psutil.AccessDenied:
                    memory_usage = 0

                # get the username of user spawned the process
                try:
                    username = process.username()
                except psutil.AccessDenied:
                    username = "N/A"

                processes.append({
                    'pid': pid, 
                    'name': name, 
                    'create_time': create_time,
                    'cores': cores,
                    'cpu_usage': cpu_usage,
                    'status': status,
                    'nice': nice,
                    'memory_usage': memory_usage,
                    'username': username
                })

        return processes

    def construct_dataframe(self, processes):
        # convert to pandas dataframe
        df = pd.DataFrame(processes)
        # set the process id as index of a process
        df.set_index('pid', inplace=True)
        # sort rows by the column passed as argument
        df.sort_values(sort_by, inplace=True, ascending=not descending)
        # pretty printing bytes
        df['memory_usage'] = df['memory_usage'].apply(get_size)
        # convert to proper date format
        df['create_time'] = df['create_time'].apply(datetime.strftime, args=("%Y-%m-%d %H:%M:%S",))
        # reorder and define used columns
        df = df[columns.split(",")]
        return df

    def run(self, params = ["python", os.path.dirname(os.path.realpath(__file__))+"apps/GUI_app.py"] ):
        """
        params: a list with the params to run on console
        examples: 
        ['python3', '-m', 'venv', 'env'] 
        ["/usr/bin/python", "-c", "print('hello')"]
        """
        p = psutil.Popen(params, stdout=PIPE)
        return p.pid


    def set_priority(self, priority_id, pid):
        """
        Changes process priority and returns an "OK" message.
        
        if there is not process associated to the PID, 
        an error message is returned.
        """
        try:
            if pid in self.__processes:
                process = psutil.Process(pid)
                process.nice(priority_id)
                return "OK"
            else:
                return "That process is not yours"
        except psutil.NoSuchProcess as e:
            return f"Error: {e}"

    def get_status(self, pid):
        """
        Returns the process status,
        if there is not process associated to the PID, 
        an error message is returned.
        """
        try:
            if pid in self.__processes:
                process = psutil.Process(pid)
                return process.status()
            else:
                return "Error: That process is not yours"
        except psutil.NoSuchProcess as e:
            return f"Error: {e}"

    def terminate(self, pid):
        """
        Given a process ID, it looks for its process and closes it. 
        """
        try:
            if pid in self.__processes:
                process = psutil.Process(pid)
                process.terminate()
                self.__processes.remove(pid)
                return "OK"
            else:
                return "Error: That process is not yours"
        except psutil.NoSuchProcess as e:
            return f"Error: {e}"
        

    def terminate_all(self):
        """
        Terminates all of the running processes and closes the app
        """
        for pid in self.__processes:
            self.terminate(pid)
        exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Viewer & Monitor")
    parser.add_argument("-c", "--columns", help="""Columns to show,
                                                available are name,create_time,cores,cpu_usage,status,nice,memory_usage,username.
                                                Default is name,cpu_usage,memory_usage,status,create_time,nice,cores.""",
                        default="name,cpu_usage,memory_usage,status,create_time,nice,cores")
    parser.add_argument("-s", "--sort-by", dest="sort_by", help="Column to sort by, default is memory_usage .", default="memory_usage")
    parser.add_argument("--descending", action="store_true", help="Whether to sort in descending order.")
    parser.add_argument("-n", help="Number of processes to show, will show all if 0 is specified, default is 10 .", default=10)
    parser.add_argument("-u", "--live-update", action="store_true", help="Whether to keep the program on and updating process information each second")

    # parse arguments
    args = parser.parse_args()
    columns = args.columns
    sort_by = args.sort_by
    descending = args.descending
    n = int(args.n)
    live_update = args.live_update

    # print the processes for the first time
    handler = AppHandler()
    processes = handler.get_processes_info()
    df = handler.construct_dataframe(processes)
    if n == 0:
        print(df.to_string())
    elif n > 0:
        print(df.head(n).to_string())
    # print continuously
    while live_update:
        # get all process info
        processes = handler.get_processes_info()
        df = handler.construct_dataframe(processes)
        # clear the screen depending on your OS
        os.system("cls") if "nt" in os.name else os.system("clear")
        if n == 0:
            print(df.to_string())
        elif n > 0:
            print(df.head(n).to_string())
        time.sleep(0.7)