//Define_pins
int motor1a = 10;
int motor1b = 11;
int motor2a = 12;
int motor2b = 13;
char input_signal;

//Pin_types
void setup()
{ 
pinMode(motor1a, OUTPUT);
pinMode(motor1b, OUTPUT);
pinMode(motor2a, OUTPUT);
pinMode(motor2b, OUTPUT);
Serial.begin(9600);
}

//Main_Body
void loop()
{
  while (Serial.available() > 0)
  {
  input_signal = Serial.read();
  Serial.println(input_signal);
  }

  if( input_signal == 'F'){
    forward();
    }
  else if(input_signal == 'B'){
    reverse();
    }
  else if(input_signal == 'L'){
    left();  
    }
  else if(input_signal == 'R'){
    right();
    }
   
  else{
    stop_working();
    }
}

//Functions

void stop_working(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, LOW);
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, LOW);
  }

void forward(){
  digitalWrite(motor1a, HIGH);
  digitalWrite(motor1b, LOW);
  digitalWrite(motor2a, HIGH);
  digitalWrite(motor2b, LOW);
  }

void reverse(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, HIGH);
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, HIGH);
  }

void left(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, HIGH);
  digitalWrite(motor2a, HIGH);
  digitalWrite(motor2b, LOW);
  }

void right(){
  digitalWrite(motor1a, HIGH);
  digitalWrite(motor1b, LOW);
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, HIGH);
  }
