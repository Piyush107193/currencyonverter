import tkinter as tk

# Manually defined exchange rates (as of a specific date, not up-to-date)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.94,
    "GBP": 0.77,
    "JPY": 149.68,
    "CAD": 1.28,
    "AUD": 1.58,
    "INR": 83.28,
    "CNY": 6.38
}

# Function to perform currency conversion
def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()

    if from_currency == to_currency:
        converted_amount.set(amount)
    else:
        converted_amount.set(round(amount * exchange_rates[to_currency] / exchange_rates[from_currency], 2))

# Create a Tkinter window
window = tk.Tk()
window.title("Currency Converter")

# Create labels, entry fields, and buttons
label_from_currency = tk.Label(window, text="From Currency:")
label_to_currency = tk.Label(window, text="To Currency:")
label_amount = tk.Label(window, text="Amount:")
label_result = tk.Label(window, text="Converted Amount:")

combo_from_currency = tk.StringVar()
combo_to_currency = tk.StringVar()
entry_amount = tk.DoubleVar()
converted_amount = tk.DoubleVar()

combo_from_currency = tk.StringVar()
combo_from_currency.set("USD")
combo_to_currency = tk.StringVar()
combo_to_currency.set("EUR")

entry_from_currency = tk.OptionMenu(window, combo_from_currency, *exchange_rates.keys())
entry_to_currency = tk.OptionMenu(window, combo_to_currency, *exchange_rates.keys())
entry_amount = tk.Entry(window, textvariable=entry_amount)
entry_result = tk.Label(window, textvariable=converted_amount)

convert_button = tk.Button(window, text="Convert", command=convert_currency)

# Arrange widgets in the window using the grid layout
label_from_currency.grid(row=0, column=0)
label_to_currency.grid(row=1, column=0)
label_amount.grid(row=2, column=0)
label_result.grid(row=3, column=0)

entry_from_currency.grid(row=0, column=1)
entry_to_currency.grid(row=1, column=1)
entry_amount.grid(row=2, column=1)
entry_result.grid(row=3, column=1)

convert_button.grid(row=4, columnspan=2)

