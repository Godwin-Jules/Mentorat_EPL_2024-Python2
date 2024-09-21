import time
import threading

# Définition de verrou
locking_process = threading.RLock()

def process_one():
    i = 0
    while i < 5:
        i += 1
        print("o"*i*2)
        time.sleep(1)

def process_two():
    i = 0
    while i < 5:
        i += 1
        print("x"*i*2)
        time.sleep(1)

class MyProcess(threading.Thread):
    #On surcharge le constructeur de la classe Thread
    def __init__(self):
        threading.Thread.__init__(self)

    #On surcharge la méthode run() qui est appelée lorsqu'on démarre le thread
    def run(self):
        i = 0
        while i < 5:
            print(threading.current_thread(), i)
            time.sleep(0.3)
            i += 1

class MyProcessAgain(threading.Thread):
    #On surcharge le constructeur de la classe Thread
    def __init__(self):
        threading.Thread.__init__(self)

    #On surcharge la méthode run() qui est appelée lorsqu'on démarre le thread
    def run(self):
        i = 0
        while i < 5:
            # Utilisation du verrou
            with locking_process:
                letters = "ABCD"
                for letter in letters:
                    print(letter, threading.current_thread().name)
                    time.sleep(0.3)
            print()
            i += 1


def main():
    # On crée nos objects threads en instanciant la classe Thread
    # th1 = threading.Thread(target=process_one)
    # th2 = threading.Thread(target=process_two)
    # th1 = MyProcess()
    # th2 = MyProcess()
    th1 = MyProcessAgain()
    th2 = MyProcessAgain()

    # On démarre les threads
    start_time = time.time()
    th1.start()
    th2.start()

    # On attend que les threads se terminent avant de continuer le programme
    th1.join()
    th2.join()
    end_time = time.time()

    # Une fois que les threads sont terminés, on affiche un message de la fin du programme
    print(f"Durée d'éxécution: {end_time - start_time:.3f} secondes")
    print("Fin du programme")



if __name__ == "__main__":
    main()