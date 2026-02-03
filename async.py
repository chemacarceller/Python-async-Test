import asyncio
import time
import requests
from threading import Thread, Timer

class AsyncTask(Thread):
    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._run())
        loop.close()

    async def _run(self):
        print("Beginning Async Task...")
        
        # Throwing an asynchronous task and wait
        await asyncio.sleep(5)
        
        # API request. The `await` block is not necessary as it is implemented automatically.
        r = requests.get("https://api.chucknorris.io/jokes/random")
        print(r.json()["value"])
        
        # The following code waits...
        print("Finished Async Task 5 seconds after")

def funcion1():
    print("Function launched with the equivalent of JavaScript's setTimeout 2 seconds later")

def worker():
    # Synchronous timer only stops this thread of execution
    time.sleep(3)
    print("Function launched with a Thread, has waited 3 seconds synchronously, only this thread of execution")


print("Beginning...")

# Javascript setTimeout equivalent, asynchronous timer
s = Timer(2.0, funcion1)
s.start()

# We launch a thread of execution; it runs asynchronously.
t = Thread(target=worker)
t.start()

# An asynchronous task is launched and you wait for it to finish.
# If it were not launched in a child execution, await would stop all code except for asynchronous functions launched in parallel.
t = AsyncTask()
t.start()

print("Ending...")
