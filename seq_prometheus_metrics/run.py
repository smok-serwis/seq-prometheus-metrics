from .fetcher import FetcherThread
from .app import WorkerThread
from satella.posix import hang_until_sig


if __name__ == '__main__':
    ft = FetcherThread()
    wt = WorkerThread()
    wt.start()
    ft.start()
    hang_until_sig()
    ft.terminate().join()
