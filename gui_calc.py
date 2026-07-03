from tkinter import*
from tkinter import messagebox
import signal
import ast


def _eval_ast(node):
    if isinstance(node, ast.BinOp):
        left = _eval_ast(node.left)
        right = _eval_ast(node.right)
        op = node.op
        if isinstance(op, ast.Add):
            return left + right
        if isinstance(op, ast.Sub):
            return left - right
        if isinstance(op, ast.Mult):
            return left * right
        if isinstance(op, ast.Div):
            return left / right
        if isinstance(op, ast.Mod):
            return left % right
        if isinstance(op, ast.Pow):
            return left ** right
        if isinstance(op, ast.FloorDiv):
            return left // right
        raise ValueError("Unsupported binary operator")
    elif isinstance(node, ast.UnaryOp):
        operand = _eval_ast(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand
        raise ValueError("Unsupported unary operator")
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only int/float constants allowed")
    elif isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Expression):
        return _eval_ast(node.body)
    else:
        raise ValueError("Unsupported expression")


def safe_eval(expr: str):
    parsed = ast.parse(expr, mode="eval")
    return _eval_ast(parsed.body)

def buttonclick(number):
    global operator
    operator= operator + str(number)
    input_value.set(operator)

def buttonclear():
    global operator
    operator= ""
    input_value.set("")
def buttonequal():
    global operator

    if not operator or operator[-1] in "+-*/.%(":
        messagebox.showerror("Error", "Invalid expression! Please complete your calculation.")
        return

    try:
        result = safe_eval(operator)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        operator = ""
        input_value.set("")
        return
    except (SyntaxError, ValueError):
        messagebox.showerror("Error", "Invalid expression! Check your input.")
        operator = ""
        input_value.set("")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Calculation error: {e}")
        operator = ""
        input_value.set("")
        return

    input_value.set(str(result))
    operator = ""

main = Tk()
main.title("CALCULATOR")
main.geometry("350x400+0+0")
main.config(bg="#202020")
main.resizable(False, False)


operator = ""
input_value= StringVar()
display_text= Entry(main, font=("arial",20,"bold"),textvariable=input_value, bd=15, insertwidth=2, bg="#202020", justify=RIGHT)
display_text.grid(columnspan=4)

#Row C % / 
btn_c= Button(main,padx=16, bd=8,fg="#CCCCCC", font=("arial", 20, "bold"),text="c",command=buttonclear)
btn_c.grid(row=1, column=0)

btn_percent=Button(main,padx=16, bd=8, fg="#ff9500", font=("arial", 20, "bold"),text="%", command=lambda: buttonclick("%"))
btn_percent.grid(row=1, column=1)

btn_brac=Button(main,padx=16, bd=8, fg="#ff9500", font=("arial", 20, "bold"),text="(", command=lambda: buttonclick("("))
btn_brac.grid(row=1, column=2)

btn_firstbrac=Button(main,padx=16, bd=8, fg="#ff9500", font=("arial", 20, "bold"),text=")", command=lambda: buttonclick(")"))
btn_firstbrac.grid(row=1, column=3)


#Row 1 7 8 9 +
btn_7= Button(main,padx=16, bd=8,fg="#cccccc", font=("arial", 20, "bold"),text="7", command=lambda:buttonclick(7))
btn_7.grid(row=2, column=0)

btn_8=Button(main,padx=16, bd=8, fg="#cccccc", font=("arial", 20, "bold"),text="8", command=lambda:buttonclick(8))
btn_8.grid(row=2, column=1)

btn_9= Button(main,padx=16, bd=8,fg="#cccccc", font=("arial", 20, "bold"),text="9", command=lambda:buttonclick(9))
btn_9.grid(row=2, column=2)

btn_multi=Button(main,padx=16, bd=8,fg="#ff9500", font=("arial", 20, "bold"),text="*", command=lambda:buttonclick("*"))
btn_multi.grid(row=2, column=3)

#Row 2- 4 5 6 -
btn_4= Button(main,padx=16, bd=8,fg="#cccccc", font=("arial", 20, "bold"),text="4", command=lambda:buttonclick(4))
btn_4.grid(row=3, column=0)

btn_5=Button(main,padx=16, bd=8, fg="#cccccc", font=("arial", 20, "bold"),text="5", command=lambda:buttonclick(5))
btn_5.grid(row=3, column=1)

btn_6= Button(main,padx=16, bd=8,fg="#cccccc", font=("arial", 20, "bold"),text="6", command=lambda:buttonclick(6))
btn_6.grid(row=3, column=2)

btn_sub=Button(main,padx=16, bd=8,fg="#ff9500", font=("arial", 20, "bold"),text="-", command=lambda:buttonclick("-"))
btn_sub.grid(row=3, column=3)

#Row 3- 1 2 3 *
btn_1= Button(main,padx=16, bd=8,fg="#cccccc", font=("arial", 20, "bold"),text="1", command=lambda:buttonclick(1))
btn_1.grid(row=4, column=0)

btn_2=Button(main,padx=16, bd=8, fg="#cccccc", font=("arial", 20, "bold"),text="2", command=lambda:buttonclick(2))
btn_2.grid(row=4, column=1)

btn_3= Button(main,padx=16, bd=8,fg="#cccccc", font=("arial", 20, "bold"),text="3", command=lambda:buttonclick(3))
btn_3.grid(row=4, column=2)

btn_add=Button(main,padx=16, bd=8,fg="#ff9500", font=("arial", 20, "bold"),text="+", command=lambda:buttonclick("+"))
btn_add.grid(row=4, column=3)

#Row 0 . = 
btn_zero= Button(main,padx=16, bd=8,fg="#cccccc", font=("arial", 20, "bold"),text="0", command=lambda:buttonclick(0))
btn_zero.grid(row=5, column=0)

btn_dot=Button(main,padx=16, bd=8, fg="#cccccc", font=("arial", 20, "bold"),text=".", command=lambda:buttonclick("."))
btn_dot.grid(row=5, column=1)

btn_div= Button(main,padx=16, bd=8,fg="#ff9500", font=("arial", 20, "bold"),text="/", command=lambda:buttonclick("/"))
btn_div.grid(row=5, column=2)

btn_eq= Button(main,padx=16, bd=8,fg="#ff9500", font=("arial", 20, "bold"),text="=", command=buttonequal)
btn_eq.grid(row=5, column=3)


if __name__ == "__main__":
    def _sigint_handler(sig, frame):
        try:
            main.quit()
        except Exception:
            pass

    signal.signal(signal.SIGINT, _sigint_handler)

    try:
        main.mainloop()
    except KeyboardInterrupt:
        try:
            main.destroy()
        except Exception:
            pass
