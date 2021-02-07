4.1 
git clone git@github.com:emilyxzhou/my-imaginary-repo.git
cd my-imaginary-repo
touch my_second_file.py
git add my_second_file.py 
git commit -s -m "Create new file"
git push 

4.2
I used Vim directly in the RPi. I'm not that familiar with the cut, copy, and paste shortcuts in Vim, and getting more practice in that would make my coding a lot more efficient. 

4.3 
The I2C communication protocol, a synchronous serial communication bus, is used to read the ultrasonic sensor output. To write to the I2C block, the grovepi library sleeps for 0.002s; to read from the I2C block, there is an additional 0.002s sleep.
