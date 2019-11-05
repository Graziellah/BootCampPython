from time import sleep
from progress.bar import FillingSquaresBar


listy = range(10000)
ret = 0


def ft_progress(biglist):
    for mot in biglist:
        yield mot


with FillingSquaresBar('Processing', max=10000) as bar:
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        bar.next()
        sleep(0.01)
print(ret)
