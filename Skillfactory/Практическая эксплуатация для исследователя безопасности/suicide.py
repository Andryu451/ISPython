import time
import os
import signal



def suicide() -> None:
    self_pid = os.getpid() # получаем айди запущенного программой процесса
 
    print('Before suicide') # для наглядности выведем сообщение перед тем, как процесс погибнет 
    time.sleep(3) # подождём три секунды, перед тем, как самоубиться
    os.kill(self_pid, signal.SIGBREAK) # убиваемся
 
    print('After suicide :)') # а вот это сообщение мы никогда не увидим, ведь программа к тому моменту уже будет мертва...
