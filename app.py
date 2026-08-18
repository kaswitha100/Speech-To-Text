import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import threading

# Speech recognizer
recognizer = sr.Recognizer()

# Stop control
stop_listening = False

# Language codes
languages = {
    "English": "en-IN",
    "Telugu": "te-IN",
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN"
}


def start_listening():
    global stop_listening
    stop_listening = False

    status_label.config(
        text="Listening... Speak now",
        fg="green"
    )

    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

    thread = threading.Thread(target=listen)
    thread.daemon = True
    thread.start()


def listen():
    global stop_listening

    selected_language = language_var.get()
    language_code = languages[selected_language]

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        while not stop_listening:

            try:
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )

                status_label.config(
                    text="Converting speech to text...",
                    fg="blue"
                )

                text = recognizer.recognize_google(
                    audio,
                    language=language_code
                )

                # Display output
                text_box.insert(
                    tk.END,
                    text + "\n"
                )

                # Save output automatically
                with open(
                    "output.txt",
                    "a",
                    encoding="utf-8"
                ) as file:
                    file.write(text + "\n")

                status_label.config(
                    text="Listening... Speak again",
                    fg="green"
                )

            except sr.WaitTimeoutError:

                status_label.config(
                    text="Waiting for speech...",
                    fg="orange"
                )

            except sr.UnknownValueError:

                status_label.config(
                    text="Could not understand. Please speak again.",
                    fg="red"
                )

            except sr.RequestError:

                status_label.config(
                    text="Internet connection problem.",
                    fg="red"
                )

            except Exception as e:

                status_label.config(
                    text="Error: " + str(e),
                    fg="red"
                )

    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

    status_label.config(
        text="Stopped",
        fg="black"
    )


def stop_listening_function():
    global stop_listening

    stop_listening = True

    status_label.config(
        text="Stopping...",
        fg="orange"
    )


def clear_text():
    text_box.delete("1.0", tk.END)

    status_label.config(
        text="Text cleared",
        fg="blue"
    )


# ---------------- GUI ----------------

root = tk.Tk()

root.title("Speech-to-Text Converter")
root.geometry("700x550")

# Title
title_label = tk.Label(
    root,
    text="Speech-to-Text Converter",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=15)


# Language label
language_label = tk.Label(
    root,
    text="Select Language:",
    font=("Arial", 12, "bold")
)

language_label.pack()


# Language selection
language_var = tk.StringVar()
language_var.set("English")

language_menu = tk.OptionMenu(
    root,
    language_var,
    *languages.keys()
)

language_menu.config(
    font=("Arial", 11, "bold"),
    bg="lightblue",
    fg="black",
    width=15
)

language_menu.pack(pady=8)


# Start button
start_button = tk.Button(
    root,
    text="Start Listening",
    font=("Arial", 13, "bold"),
    bg="green",
    fg="white",
    activebackground="darkgreen",
    activeforeground="white",
    width=18,
    command=start_listening
)

start_button.pack(pady=8)


# Stop button
stop_button = tk.Button(
    root,
    text="Stop Listening",
    font=("Arial", 13, "bold"),
    bg="red",
    fg="white",
    activebackground="darkred",
    activeforeground="white",
    width=18,
    state=tk.DISABLED,
    command=stop_listening_function
)

stop_button.pack(pady=5)


# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="orange",
    fg="white",
    activebackground="darkorange",
    activeforeground="white",
    width=18,
    command=clear_text
)

clear_button.pack(pady=5)


# Status label
status_label = tk.Label(
    root,
    text="Select language and click Start Listening",
    font=("Arial", 11, "bold"),
    fg="black"
)

status_label.pack(pady=10)


# Text box
text_box = scrolledtext.ScrolledText(
    root,
    width=70,
    height=15,
    font=("Arial", 12)
)

text_box.pack(
    padx=20,
    pady=10
)


# Start application
root.mainloop()