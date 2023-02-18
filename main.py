from frames_to_array import frame_to_array
import pyautogui, pyperclip
import time

def substitute(string, sub):
    return ''.join([sub.get(c,c) for c in string])

def get_tetrio_map(image_path, scaling):
    image_array = frame_to_array(image_path, scaling)
    #print(arr.shape)
    final = ["_" * board_padding + substitute("".join([str(i) for i in row]) + "_" * board_padding, {"0":blank, "1":grey}) for row in image_array]

    tetrio_map = "_" * board_width * board_padding + "".join(final) + "_" * board_width * board_padding
    return tetrio_map

def do_macro_round(frame_number):
    # copy the tetrio map into clipboard
    tetrio_map = get_tetrio_map(f"./frames/{frame_number}.jpg", scaling)
    pyperclip.copy(tetrio_map)

    pyautogui.click(x=814, y=709) # click SOLO
    time.sleep(0.5)
    pyautogui.click(x=874, y=578) # click CUSTOM
    time.sleep(0.5)
    pyautogui.click(x=1548, y=370) # click OBJECTIVE (custom game settings)
    time.sleep(0.1)
    pyautogui.click(x=606, y=606)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.typewrite(str(frame_number)) # type frame number into line goal count
    time.sleep(0.1)
    pyautogui.click(x=2274, y=369) # click META (custom game settings)
    pyautogui.click(x=2274, y=369) # click META (custom game settings)
    time.sleep(0.1)
    pyautogui.click(x=733, y=501) # click CUSTOM GAME STRING
    pyautogui.click(x=733, y=501) # click CUSTOM GAME STRING
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(x=2495, y=296) #click START
    time.sleep(2)
    pyautogui.moveTo(3200, 0) # move mouse away, ready to take screenshot
    time.sleep(0.1)
    screenshot = pyautogui.screenshot(region=(0, 0, 3045, 1401)) # take screenshot
    screenshot.save(f"./screenshots/{frame_number}.png") # save screenshot
    time.sleep(0.1)
    pyautogui.keyDown('esc') # exit out of the game
    time.sleep(1.5)
    pyautogui.keyUp('esc')


# custom map things 
grey = "#"
blank = "_"

scaling = 1/6
board_padding = 3
board_width = 80 + board_padding * 2
board_height = 60 + board_padding * 2


time.sleep(3) # macro starting delay

total_frames = 6572
for frame_number in range(1, total_frames + 1):
    start_time = time.perf_counter()

    do_macro_round(frame_number)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"done frame {frame_number} in {elapsed_time:.2f} seconds")