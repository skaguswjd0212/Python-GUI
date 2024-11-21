from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
import pickle
import os.path


window=Tk()
window.title("Start!")
window.geometry("200x100+820+100")
window.configure(bg="lavender")
window.resizable(False, False)

i=1
Width=50
photo=PhotoImage(file="나.png")
plan=[""]

    
def main():    
    window.geometry("150x20+0+0")
    toplevel =Toplevel(window)
    toplevel.title("Draw it!")
    toplevel.geometry("1000x500+20+100")    
    
    #프레임 나누기(f1, canvas, f2)
    frame1=Frame(toplevel , relief="solid", bd=2, width=200, height=550)
    frame1.grid(row=0, column=0)
    canvas = Canvas(toplevel , relief = "solid", bd = 2, width=400, height=550, scrollregion=(0,0,500,500))
    canvas.grid(row=0, column=1)
    frame2=Frame(toplevel , relief="solid", bd=2, width=100, height=550)
    frame2.grid(row=0, column=2)
    
    #window

    #선 두께 변화를 화면에 label
    def scroll(event):
        global Width
        if event.delta==120:
            Width+=1
        if event.delta==-120:
            Width-=1
        l12.config(text="선 두께: "+str(Width))
    l12=Label(toplevel , text="선 두께: "+str(Width), font="HY목각파임B", bg="burlywood", fg="black")
    l12.grid(row=1, column=1)
    canvas.bind("<MouseWheel>", scroll)
    
    #배경색 초기 지정
    canvas.configure(bg="lightblue")
    frame1.configure( bg="lavender")
    toplevel.configure(bg="snow")
    frame2.configure(bg="white")
    
    #외부 윈도우 설정 1
    function = Toplevel(window)
    function.title("Draw it! 추가 기능")
    function.resizable(False, False)
    function_l1=Label(function, text="Draw it!의 색깔 바꾸기 기능을 활용해보세요.")
    function.geometry("400x345+1100+100")
    button_dict = {'빨간색':'red', '주황색':'orange', '노랑색':'yellow', '초록색':'green', '파란색':'blue',
               '보라색':'violet',' 분홍색':'pink','갈색':'brown', '검정색':'black', '회색':'gray', '금색':'gold',
               '은색':'silver', '흰색':'white', '카키색':'khaki', '하늘색':'skyblue', '청록색':'cyan',
               '밝은 보라색':'lavender','연두색':'yellowgreen', '남색':'navy', '올리브색':'olive' }
    row_index = 1
    col_index = 0
    
    #click(t) 함수 지정, 마우스 이벤트
    def click(w):
        def drawing(event):
            if Width>0:
                x1=event.x-Width
                y1=event.y-Width
                x2=event.x+Width
                y2=event.y+Width
                canvas.create_oval(x1, y1, x2, y2, fill=button_dict[w], outline=button_dict[w])
        canvas.bind("<B1-Motion>", drawing)
        def circle(event):
            if Width>0:
                x1=event.x-Width
                y1=event.y-Width
                x2=event.x+Width
                y2=event.y+Width
                canvas.create_oval(x1, y1, x2, y2, fill=button_dict[w], outline=button_dict[w])
        canvas.bind("<Double-Button-1>", circle)

        def rectangle(event):
            if Width>0:
                x1=event.x-Width
                y1=event.y-Width
                x2=event.x+Width
                y2=event.y+Width
                canvas.create_rectangle(x1, y1, x2, y2, fill=button_dict[w], outline=button_dict[w])
        canvas.bind("<Double-Button-3>", rectangle)
        
    #외부 윈도우 설정 2
    for Buttontext in button_dict:
        def process(t=Buttontext):
            click(t)
        Button(function, text=Buttontext, width=10, height=5, bg=button_dict[Buttontext], command=process).grid(row=row_index, column=col_index)
        col_index += 1
        if col_index > 4:
            row_index += 1
            col_index = 0
                
    #초기화 버튼, 함수
    def reset():
        canvas.delete("all")
    b5=Button(toplevel , text="초기화", command=reset, font="궁서체", fg="black", bg="red")
    b5.grid(row=2, column=1)


    
    #frame1
    #오늘의 계획 라벨
    l7=Label(frame1, text="☆오늘의 계획☆", font="휴먼둥근헤드라인", fg='mediumpurple', bg="lavender")
    l7.grid(row=0, column=0, columnspan=2)
    
    #일정추가 안내 라벨
    l8=Label(frame1, text="일정을 입력하세요.\n(5개까지 입력가능합니다.)", font="휴먼편지체", bg="snow", fg="black")
    l8.grid(row=7, column=0, columnspan=3)

    #일정 인덱스 입력 엔트리
    e2=Entry(frame1, width=3)
    e2.grid(column=0, row=8, sticky="e")

    #일정 내용 입력 엔트리
    e1=Entry(frame1)
    e1.grid(column=2, row=8, sticky="e")

    #동기부여 label
    l9=Label(frame1, text="파이팅!! 당신은 할 수 있어요!", font="휴먼둥근헤드라인", bg="yellow", fg="orange")
    l9.grid(column=0, row=6, columnspan=3)

    #일정 완료 동작
    def run(x):
        if x==True:
            l9.config(text="잘했어요!\n언제나 노력하는 당신, 정말 멋져요!")
        else:
            l9.config(text="파이팅! 당신은 할 수 있어요!")

    #plan 체크박스
    chk_state1= BooleanVar()
    chk_state1.set(False)
    c1= Checkbutton(frame1, text="", var=chk_state1, bg="burlywood", command=lambda: run(chk_state1.get()))
    c1.grid(column=0, row=1, columnspan=2)

    chk_state2= BooleanVar()
    chk_state2.set(False)
    c2= Checkbutton(frame1, text="", var=chk_state2, bg="burlywood",command=lambda: run(chk_state2.get()))
    c2.grid(column=0, row=2, columnspan=2)

    chk_state3= BooleanVar()
    chk_state3.set(False)
    c3= Checkbutton(frame1, text="", var=chk_state3, bg="burlywood",command=lambda:run(chk_state3.get()))
    c3.grid(column=0, row=3, columnspan=2)

    chk_state4= BooleanVar()
    chk_state4.set(False)
    c4= Checkbutton(frame1, text="", var=chk_state4, bg="burlywood", command=lambda:run(chk_state4.get()))
    c4.grid(column=0, row=4, columnspan=2)

    chk_state5= BooleanVar()
    chk_state5.set(False)
    c5= Checkbutton(frame1, text="", var=chk_state5, bg="burlywood", command=lambda:run(chk_state5.get()))
    c5.grid(column=0, row=5, columnspan=2)

    #일정 추가 버튼 동작
    def plus():
        global plan
        plus_index=int(e2.get())
        plan.insert(plus_index, e1.get())
        if plus_index==1:
            c1.configure(text=plan[1])
        elif plus_index==2:
            c2['text']=plan[2]
        elif plus_index==3:
            c3['text']=plan[3]
        elif plus_index==4:
            c4['text']=plan[4]
        elif plus_index==5:
            c5['text']=plan[5]
        e1.delete(0, 'end')
        e2.delete(0, 'end')

    #일정 삭제 버튼 동작
    def minus():
        global plan
        minus_index=int(e2.get())
        if minus_index==1:
            c1.configure(text="")
            chk_state1.set(False)
        elif minus_index==2:
            c2['text']=""
            chk_state2.set(False)
        elif minus_index==3:
            c3['text']=""
            chk_state3.set(False)
        elif minus_index==4:
            c4['text']=""
            chk_state4.set(False)
        elif minus_index==5:
            c5['text']=""
            chk_state5.set(False)
        e1.delete(0, 'end')
        e2.delete(0,'end')
        
    #일정추가 버튼
    b3=Button(frame1, text="추가", command=plus, font="휴먼편지체", bg="white")
    b3.grid(row=9, column=2, sticky="w")
    
    #일정 삭제버튼
    b4=Button(frame1, text="삭제", command=minus, font="휴먼편지체", bg="white")
    b4.grid(row=9, column=1, sticky="e")
    
    #일정 항목 안내 label
    l10=Label(frame1, text="번째 항목",  bg="lavender", font="휴먼편지체")
    l10.grid(row=8, column=1)
    
    #이미지
    global photo
    l11=Label(frame1, image=photo, height=200)
    l11.grid(row=10, column=0,columnspan=4)


                 
    #frame2
    #아이디어 노트 만들기
    l2=Label(frame2, text="나만의 아이디어 노트!", font="휴먼편지체", bg="lightblue", fg="blue", width=60)
    l2.grid(row=0, column=1, columnspan=3)
    txt = scrolledtext.ScrolledText(frame2, width=80,height=5)
    txt.grid(row=1, column=1, columnspan=3)

    
    def del_text():
        txt.delete(1.0,'end')
        
    def save():
        f='idea_note_all.txt'
        if os.path.isfile(f):
            f=open('idea_note_all.txt','a', encoding='UTF8')
            f.write(txt.get(1.0,'end'))
        else:
            f=open('idea_note_all.txt','w', encoding='UTF8')
            f.write(txt.get(1.0,'end'))
        f.close()
        file='idea_note.txt'
        infile=open(file,'w', encoding='UTF8')
        infile.write(txt.get(1.0,'end'))
        infile.close()
        messagebox.showinfo('Save', '저장 완료!')
            
    b6=Button(frame2, text="지우기", command=del_text, font="휴먼편지체", bg="lightblue", fg="blue")
    b6.grid(row=2, column=2, sticky="w")
    b7=Button(frame2, text="저장하기", command=save, font="휴먼편지체", bg="lightblue", fg="blue")
    b7.grid(row=2, column=2, sticky="e")
    
    #오늘의 명언 라벨
    l1=Label(frame2, text="♣오늘의 명언♣", font="궁서체",fg="forestgreen", bg="burlywood", width=60)
    l1.grid(row=3, column=1, columnspan=3)
    l3=Label(frame2, width=60, text='"네가 원하는 그 자리를 단 한 명만 뽑는다면\n그 한 명이 무조건 네가 되도록 만들어라."', font="궁서체",fg="forestgreen", bg="wheat")
    l3.grid(row=4, column=1, columnspan=3)
    
    #오늘의 명언 넘기기
    l4=Label(frame2, text=str(i)+" / "+str(10), bg="white")
    say=['', '"네가 원하는 그 자리를 단 한 명만 뽑는다면\n 그 한 명이 무조건 네가 되도록 만들어라."',
     '"노력을 이기는 재능은 없고\n노력을 외면하는 결과도 없다."','"절대 후회하지 마라.\n 좋았다면 추억이고\n나빴다면 경험이다."','"우리가 이룬 것들은 그동안 견뎌온 어려움 덕분이다."','"변화와 성장은 늘 한계점에서 이루어진다."','"지나간 시간은 다시 돌아오지 않는다."','"어느날 갑자기, 하루아침에 \n극적인 변화가 일어나는 일은 없다."','"인간을 성공으로 이끄는 \n가장 강력한 무기는 \n바로 습관이다."','"뭐든 생각하기 나름이야!"', '"뛰어난 사람이 아니라 \n쉬지 않고 가는 사람이 \n결국에는 원하는 것을 이룬다."']


    #오늘의 명언 버튼1
    def page_previous():
        global i
        i=i-1
        if i<1:
            i=i+10
            l4['text']=i, "/", 10
            l3['text']=say[i]
        else:
            l4['text']=i, "/", 10
            l3['text']=say[i]
            
    b1=Button(frame2, text="◀", command=page_previous, bg="white")
    l4.grid(row=5, column=2)
    b1.grid(row=5, column=1, sticky="e")
    
    #오늘의 명언 버튼2
    def page_next():
        global i
        i=i+1
        if i>10:
            i=i-10
            l4['text']=i, "/", 10
            l3['text']=say[i]
        else:
            l4['text']=i, "/", 10
            l3['text']=say[i]
    b2=Button(frame2, text="▶", command=page_next, bg="white")
    b2.grid(row=5, column=2, sticky="e" )
    
    #당부 Run!
    l6=Label(frame2, text="그럼 오늘도 Draw it과 함께 열심히 달려보아요!",font="휴먼편지체", bg="peachpuff", fg="purple", width=60, height=3)
    l6.grid(row=8, column=1, columnspan=3)
    
    #사용설명서
    l5=Label(frame2, font="휴먼편지체", fg="black", bg="cyan", width=60, text="Drawit! 프로그램 사용 설명서")
    l5.grid(row=6, column=1, columnspan=3)
    l13=Label(frame2, font="휴먼편지체", fg="black", bg="snow", width=60, text="①추가 기능 창에서 원하는 색깔 클릭!\n②마우스 스크롤로 두께 조절        \n③드래그->드로잉 기능           \n④마우스 왼쪽 버튼 더블 클릭-> 원그리기\n④마우스 오른쪽 버튼 더블 클릭-> 사각형그리기")
    l13.grid(row=7, column=1, columnspan=3)


    #메뉴
    #함수 정의
    def open_file():
        file=filedialog.askopenfilename()
        if file[len(file)-3:len(file)]=='txt':
            infile=open(file, "r", encoding="UTF8")
            lines=infile.read()
            txt.insert(INSERT, lines)
            txt.see(END)

        elif file[len(file)-1:len(file)]=='p':
            infile=open(file, "rb")
            lines=pickle.load(infile)
            txt.insert(INSERT, lines)
            txt.see(END)


    def close_file():
        res=messagebox.askquestion("Close", "프로그램을 종료하시겠습니까?")
        if res=="yes":
            window.quit()
            window.destroy()

    def img_in():
        path=filedialog.askopenfilename()
        img=PhotoImage(file=path)
        l11.configure(image=img)
        l11.image=img

    def change_theme(x):
        if x==1:
            l2.config(bg="lightgoldenrodyellow", fg="darkgreen")
            l7.config(bg="mistyrose", fg="crimson")
            l10.config(bg="mistyrose")
            frame1.config(bg="mistyrose")
            canvas.config(bg="aliceblue")
            l5.config(bg="coral")
            b7.config(bg="lightgoldenrodyellow", fg="darkgreen")
            b6.config(bg="lightgoldenrodyellow", fg="darkgreen")

        elif x==3:
            l2.config(bg="mediumpurple", fg="white")
            l7.config(fg="saddlebrown", bg="cornsilk")
            l10.config(bg="linen")
            frame1.config(bg="linen")
            canvas.config(bg="beige")
            l5.config(bg="cornsilk")
            b7.config(bg="mediumpurple", fg="white")
            b6.config(bg="mediumpurple", fg="white")

        elif x==4:
            l2.config(bg="ghostwhite", fg="navy")
            l7.config(fg="darkblue", bg="lightsteelblue")
            l10.config(bg="lightblue")
            frame1.config(bg="lightblue")
            canvas.config(bg="aliceblue")
            l5.config(bg="skyblue")
            b7.config(bg="ghostwhite", fg="navy")
            b6.config(bg="ghostwhite", fg="navy")


        else:
            l2.config(bg="lightblue", fg="blue")          
            l7.config( fg='mediumpurple', bg="lavender")
            l10.config(bg="lavender")
            frame1.config(bg="lavender")
            canvas.config(bg="lightblue")
            l5.config(bg="cyan")
            b7.config(bg="lightblue", fg="blue")
            b6.config(bg="lightblue", fg="blue")
    
        
    #메뉴1 (불러오기, 저장, 종료)
    menu=Menu(toplevel)
    menu1 = Menu(menu, tearoff = 0, selectcolor="red", font="휴먼편지체")
    menu1.add_radiobutton(label = "불러오기", command=open_file)
    menu1.add_radiobutton(label = "종료하기", command=close_file)
    menu.add_cascade(label="파일", menu=menu1)

    #메뉴2 (이미지 변경)
    menu2 = Menu(menu, tearoff = 0,  selectcolor="red", font="휴먼편지체")
    menu2.add_radiobutton(label = "이미지변경", command=img_in)
    menu.add_cascade(label="편집", menu=menu2)


    #메뉴3 (테마 변경)
    menu3 = Menu(menu, tearoff = 0, selectcolor="red", font="휴먼편지체")
    menu3.add_radiobutton(label = "봄", command=lambda:change_theme(1))
    menu3.add_radiobutton(label = "여름", command=lambda:change_theme(2))
    menu3.add_radiobutton(label = "가을", command=lambda:change_theme(3))
    menu3.add_radiobutton(label = "겨울", command=lambda:change_theme(4))
    menu.add_cascade(label="테마 변경", menu=menu3)




    toplevel.config(menu=menu)
   



#로그인 함수 정의
def login():
    if sid.get()=='cse' and spw.get()=='1234':
        messagebox.showinfo('success', '        로그인 성공!\n\n창을 최대화해서 사용하세요.', command=main())
    else:
        messagebox.showinfo('fail', '로그인 실패!')

        
#메인코드

logo=Label(window, text='Draw it!', font="휴먼편지체", fg='mediumpurple', bg="lavender")
sid=Entry(window)
spw=Entry(window, show='●')
btn1=Button(window, text='LOGIN', font="휴먼편지체", bg='mediumpurple', fg='white', command=login)
logo.grid(row=0, column=0, columnspan=2)
sid.grid(row=1, column=1)
spw.grid(row=2, column=1)
btn1.grid(row=3, column=1)
l14=Label(window, text="아이디", bg="lavender")
l15=Label(window, text="비밀번호", bg="lavender")
l14.grid(row=1, column=0)
l15.grid(row=2, column=0)





window.mainloop()
