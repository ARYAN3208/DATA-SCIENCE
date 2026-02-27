{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "142f9651",
   "metadata": {},
   "source": [
    "When to Use Multithreading\n",
    "Understanding when to use multithreading is crucial. There are two main reasons:\n",
    "\n",
    "I/O Bound Tasks: Tasks that spend more time waiting for I/O operations, such as file operations or network requests.\n",
    "Concurrent Execution: When you want to improve the throughput of your application by performing multiple operations concurrently."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45a5716e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import threading\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f7e4bd59",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_numbers():\n",
    "    for i in range (5):\n",
    "        print(\"Number:{i}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8d2237cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_letter():\n",
    "    for letter in \"abcde\":\n",
    "        print(\"Letter:{letter}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ef08ca39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number:{i}\n",
      "Number:{i}\n",
      "Number:{i}\n",
      "Number:{i}\n",
      "Number:{i}\n",
      "Letter:{letter}\n",
      "Letter:{letter}\n",
      "Letter:{letter}\n",
      "Letter:{letter}\n",
      "Letter:{letter}\n"
     ]
    }
   ],
   "source": [
    "print_numbers()\n",
    "print_letter()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddf70e53",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "141afd4e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccae5703",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64f64629",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
