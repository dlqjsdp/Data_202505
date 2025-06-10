import tkinter as tk

# 1. 창 생성
root = tk.Tk()
root.title("간단한 버튼 예제")
root.geometry("300x150")  # 창 크기 지정

# 2. 버튼 클릭 시 실행할 함수 정의
def on_button_click():
    print("버튼이 클릭되었습니다!")

# 3. 버튼 생성 및 이벤트 연결
button = tk.Button(root, text="클릭하세요", command=on_button_click)

# 4. 버튼 배치
button.pack(pady=20)

# 5. GUI 이벤트 루프 시작
root.mainloop()