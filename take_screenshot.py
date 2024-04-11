import schedule
import os
import time
import pyautogui
import datetime

def take(dir_name:str):
    try:
        screenshot = pyautogui.screenshot()
        #日付でフォルダを作成
        dt_now = datetime.datetime.now()
        png_name = dt_now.strftime('%H:%M:%S')
        screenshot.save(f"out/{dir_name}/{png_name}.png")
    except:
        pass
    
def main():
    #日付でフォルダを作成
    dt_now = datetime.datetime.now()
    tmp_dir_name = dt_now.strftime('%Y年%m月%d日%H:%M:%S')
    os.mkdir(f"out/{tmp_dir_name}")
    
    start_time = time.perf_counter()
    
    #3分ごとに定期実行
    schedule.every(3).minutes.do(take,dir_name=tmp_dir_name)
    
    while True:
        schedule.run_pending()
        
        current_time = time.perf_counter()
        #90分を超えると終了
        if((current_time-start_time)/60>100):
            print(f"現在時刻：{current_time}")
            print("end")
            break
            
if __name__=='__main__':
    main() 