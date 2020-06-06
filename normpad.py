import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()    #required for tkinter app to work
main_application.geometry('1200x800')    #set the area
main_application.title('Normpad Text editor')  #showes the title


################################### main menu ############################################
#--------------------------$$$$$$$$ End main menu $$$$$$$$$$$-----------------------------
main_menu = tk.Menu()

####file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')    ######here ends icons

file = tk.Menu(main_menu, tearoff=False)  #variables for the main menu

#########Edit
#edit icons
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)   #variables for the main menu


#####View
#View icons
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')

view = tk.Menu(main_menu,tearoff=False)    #variables for the main menu

#####color theme
#Color theme icons

light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')

color_theme = tk.Menu(main_menu,tearoff=False) # here ends the vars for main menu if dont you use tearoff it can be removed

theme_choice = tk.StringVar()
#A tuple of themes
color_icons = (light_default_icon, light_plus_icon, monokai_icon, red_icon, dark_icon, night_blue_icon)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Monokai': ('#d3b774', '#474747'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Night Blue' : ('#ededed', '#6b9dc2')
}
count = 0


# cascade: adding this to the main application navigation bar
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color theme', menu=color_theme)


################################### Tool Bar ############################################

tool_bar = ttk.Label(main_application)    #creates tool bar
tool_bar.pack(side=tk.TOP, fill=tk.X)     #fills the space and places it under the main menu

# font box
font_tuples = tk.font.families()          #getting all font and storing it into a new tuple
font_family = tk.StringVar()              #chosing the font
font_box = ttk.Combobox(tool_bar, textvariable=font_family, state='readonly')    #a combo bos created
font_box['values'] = font_tuples          #value of combobox taken from tuple of fonts
font_box.current(font_tuples.index('Arial'))   #sets the default font to arial
font_box.grid(row=0, column=0, padx=5)      #placeing the combobox on the application

#Font size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(4,80,2))
font_size.current(5)
font_size.grid(row=0, column=1, padx=5)

#bold button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid( row=0, column=2, padx=5)

#italic button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid( row=0, column=3, padx=5)

#underline button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid( row=0, column=4, padx=5)

#overstrike button
overstrike_icon = tk.PhotoImage(file='icons2/overstrick.png')
overstrike_btn = ttk.Button(tool_bar, image=overstrike_icon)
overstrike_btn.grid( row=0, column=5, padx=5)

#font color button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid( row=0, column=6, padx=5)

# align left
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid( row=0, column=7, padx=5)

# align center
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid( row=0, column=8, padx=5)

# align right
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid( row=0, column=9, padx=5)

#--------------------------$$$$$$$$ End Tool Bar $$$$$$$$$$$-----------------------------

################################### Text Editor ############################################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview())
text_editor.config(yscrollcommand=scroll_bar.set)

# Font family and Font size funtionality
current_font_family = 'Arial'
current_font_size = 14
def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)   #bind the funtion to the font box without this the funtion will not work for the font change
font_size.bind("<<ComboboxSelected>>", change_font_size)

# Buttons functionality

#bold button functionality
text_property = tk.font.Font(font=text_editor['font'])
current_font_weight = text_property.actual()['weight']
current_font_slant = text_property.actual()['slant']

def change_bold():
    global text_property,current_font_weight
    text_property = tk.font.Font(font=text_editor['font'])
    current_font_weight = text_property.actual()['weight']
    current_font_slant = text_property.actual()['slant']
    if current_font_weight == 'normal':
       # print("im in bold")
        current_font_weight = 'bold'
        #text_editor.configure(font=(current_font_family, current_font_size,current_font_weight,current_font_slant))
    elif current_font_weight == 'bold':
        current_font_weight = 'normal'
        #print("imin normal")
        #text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

    text_editor.configure(font=(current_font_family, current_font_size, current_font_weight, current_font_slant))

bold_btn.configure(command=change_bold)

#italic functionality
def change_italic():
    global text_property,current_font_slant
    text_property = tk.font.Font(font=text_editor['font'])
    current_font_slant = text_property.actual()['slant']
    current_font_weight = text_property.actual()['weight']
    if current_font_slant == 'roman':
        current_font_slant = 'italic'
       # text_editor.configure(font=(current_font_family, current_font_size,'italic'))
    elif current_font_slant == 'italic':
        current_font_slant = 'roman'
       # text_editor.configure(font=(current_font_family, current_font_size, 'roman'))
    text_editor.configure(font=(current_font_family, current_font_size, current_font_weight, current_font_slant))

italic_btn.configure(command=change_italic)

# underline functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size,'underline'))
    elif text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)

def change_overstrike():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['overstrike'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size,'overstrike'))
    elif text_property.actual()['overstrike'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

overstrike_btn.configure(command=change_overstrike)

# font color functionality

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

# align functionality
#left
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

#center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

#right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)


text_editor.configure(font=('Arial', 14))

#--------------------------$$$$$$$$ End Text Editor $$$$$$$$$$$-----------------------------


################################### status bar ############################################

status_bar = ttk.Label(main_application, text= 'Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c').replace(' ', ''))
        status_bar.config(text=f'Characters : {characters} Words : {words}' )
        text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)
#--------------------------$$$$$$$$ End status bar $$$$$$$$$$$-----------------------------


################################### main menu functionality############################################

## variable
url = ''

# new functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

####adding file commands to file navigation
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='ctrl+N', command=new_file)

# open functionality

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File', filetypes=(('Text File', '*.txt'),('All Files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))



file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='ctrl+O',command=open_file)

# save file

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt', filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.colse()
    except:
        return




file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='ctrl+S',command=save_file)

# save as functionality

def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='ctrl+alt+S', command = save_as)

# exit functionality

def exit_func(event = None):
    global  url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('warning', 'Do you want to save the file ?')
            if mbox is True:
                save_file()
                main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='ctrl+Q',command = exit_func) ###here ends adding commands to file nav

#adding edit commands to the edit nav
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound= tk.LEFT, accelerator='ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear all', image=clear_all_icon,compound=tk.LEFT, accelerator='ctrl+alt+x', command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon,compound=tk.LEFT, accelerator='ctrl+F')
###$$$$here ends edit

#adding view commands to view nav
view.add_checkbutton(label='Satutus bar', image=status_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Tool bar', image=tool_bar_icon, compound=tk.LEFT)
#view ends here

#color theme command
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable= theme_choice, compound=tk.LEFT)
    count += 1

#--------------------------$$$$$$$$ End main menu functionality$$$$$$$$$$$-----------------------------

main_application.config(menu=main_menu)
main_application.mainloop()
