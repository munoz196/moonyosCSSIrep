console.log ('script running!');

let name = 'Charlie';
console.log ('Hello ' + name + '!');
let age = 15;
console.log ('You are ' + age + ' years old!');

if (age >= 16){
  console.log ('I can drive');
}
else {
  console.log('I cannot drive');
}

let money = 1500;
if (money >=1400){
  console.log ('I can buy ricky');
} else {
  console.log ('I cannot buy ricky :/');
}

const greetPeople = (name1,name2)=> {
  console.log ('Hello ' + name1 +' and '+ name2 + ' ! ');
}

const getFullName= (firstName,lastName) => {
  return firstName + ' ' + lastName;
}
let radius = 10;
let area = Math.PI * radius * radius ;
radius = radius * 2;
area = Math.PI * Math.pow(radius,2);
let width = Math.round(Math.random()* 100);
let height = Math.round(Math.random ()*50);
let circumference = width * 2 + height * 2;

setInterval (increaseNumber, 1000);
