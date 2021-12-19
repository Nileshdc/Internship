{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cb6243c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Please enter any Number to find factorial : 5\n",
      "The factorial of 5  = 120\n"
     ]
    }
   ],
   "source": [
    "import math \n",
    "\n",
    "number = int(input(\" Please enter any Number to find factorial : \"))\n",
    "\n",
    "fact = math.factorial(number)\n",
    "print(\"The factorial of %d  = %d\" %(number, fact))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c51a7165",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any number : 25\n",
      "25 is NOT a prime number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter any number : \"))\n",
    "if num > 1:\n",
    "    for i in range(2, num):\n",
    "        if (num % i) == 0:\n",
    "            print(num, \"is NOT a prime number\")\n",
    "            break\n",
    "    else:\n",
    "        print(num, \"is a PRIME number\")\n",
    "elif num == 0 or 1:\n",
    "    print(num, \"is a neither prime NOR composite number\")\n",
    "else:\n",
    "    print(num, \"is NOT a prime number it is a COMPOSITE number\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7b4c73b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a letter:DAD\n",
      "The letter is a palindrome\n"
     ]
    }
   ],
   "source": [
    "string=input((\"Enter a letter:\"))  \n",
    "if(string==string[::-1]):  \n",
    "      print(\"The letter is a palindrome\")  \n",
    "else:  \n",
    "      print(\"The letter is not a palindrome\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "15389400",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-0f3bc5313b9b>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-0f3bc5313b9b>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    14. Write a Python program to get the third side of right-angled triangle from two given sides.\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "14. Write a Python program to get the third side of right-angled triangle from two given sides.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ac6157b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hypotenuse = 5.0\n",
      "Adjacent = 4.0\n",
      "Opposite = 3.0\n",
      "You know the answer!\n"
     ]
    }
   ],
   "source": [
    "def pythagoras(opposite_side,adjacent_side,hypotenuse):\n",
    "        if opposite_side == str(\"x\"):\n",
    "            return (\"Opposite = \" + str(((hypotenuse**2) - (adjacent_side**2))**0.5))\n",
    "        elif adjacent_side == str(\"x\"):\n",
    "            return (\"Adjacent = \" + str(((hypotenuse**2) - (opposite_side**2))**0.5))\n",
    "        elif hypotenuse == str(\"x\"):\n",
    "            return (\"Hypotenuse = \" + str(((opposite_side**2) + (adjacent_side**2))**0.5))\n",
    "        else:\n",
    "            return \"You know the answer!\"\n",
    "    \n",
    "print(pythagoras(3,4,'x'))\n",
    "print(pythagoras(3,'x',5))\n",
    "print(pythagoras('x',4,5))\n",
    "print(pythagoras(3,4,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "65b48eea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the string p=1\n",
      "Character and their frequency\n",
      "p=1\n",
      "==1\n",
      "1=1\n"
     ]
    }
   ],
   "source": [
    "string=input(\"Enter the string \")\n",
    "freq=[None]*len(string)\n",
    "for i in range(0,len(string)):\n",
    "  freq[i]=1\n",
    "  for j in range(i+1,len(string)):\n",
    "    if(string[i]==string[j]):\n",
    "        freq[i]=freq[i]+1\n",
    "        string=string[:j]+'0'+string[j+1:];\n",
    "print(\"Character and their frequency\");\n",
    "for i in range(0,len(freq)):\n",
    "    if(string[i]!=' ' and string[i]!='0'):\n",
    "        print(string[i]+\"=\"+str(freq[i]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1912b06c",
   "metadata": {},
   "source": [
    "### "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "961cbbd7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32a2b636",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
