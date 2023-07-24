import time
import threading
import keyboard
import pyautogui

click_coords = []

def set_click_coords():
    global click_coords
    while True:
        if keyboard.is_pressed("f2"):
            click_coords.append(pyautogui.position())
            print(f"Координаты клика добавлены: {click_coords}")
            time.sleep(0.2)

def click_loop():
    global click_coords
    while True:
        if keyboard.is_pressed("f3"):
            print("Нажата клавиша F3. Клики будут остановлены.")
            break

        if len(click_coords) == 2:
            for coords in click_coords:
                pyautogui.click(coords[0], coords[1])
                print(f"Клик выполнен по координатам: {coords}")
        else:
            print("Ожидание координат клика...")

        time.sleep(50)  # Подождать 1 минуту перед следующим кликом

if __name__ == "__main__":
    print("Для добавления координат клика нажмите клавишу F2.")
    set_coords_thread = threading.Thread(target=set_click_coords)
    click_thread = threading.Thread(target=click_loop)

    set_coords_thread.start()
    click_thread.start()
