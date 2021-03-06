// https://projecteuler.net/problem=27

function primeTest (value) {
  if (value<=3) {return value>1;} 
  if (value%2===0||value%3===0) {return false;}
  
  /*all primes over 3 are in the form 6k+1,6k-1
  we check each value for divisibilty by these potential
  prime numbers*/
  let i=5;
  while (i**2<=value ) {
    if (value%i===0 || value%(i+2)===0) {return false;}
    i+=6
  };
  return true
}

function quadratic (a, b, n) {
  return n**2+a*n+b;
};

var A=0;var B=0; var primeCount=0;
let output = [[A,B,primeCount]]

for (a=-1000;a<1000;a++) {
  for (b=-1000;b<=1000;b++) {
    let n=0; let tempPrimeCount=-1;
    do {
      result = primeTest(quadratic(a,b,n));
      if (result===true) {
        tempPrimeCount+=1;
        n+=1;
      }
    }
    while (result!=false);
    
    if (tempPrimeCount>output[0][2]) {
          output[0][0]=a;
          output[0][1]=b;
          output[0][2]=tempPrimeCount;
    }     
  }  
}

console.log(output);

//first time using javascript to solve something
//this program takes some time to finish because of the nested for-loop
//y = x^2 -61x +971 produces 70 consecutive prime numbers







// let counter = 0;
// let value = 10001;
// for (i=1;i<value;i++){
//   // console.log(i, primeTest(i));
//   if (primeTest(i)){
//     counter+=1;
//   }  
// }
// console.log('The total number of primes less than '+value+' is ' + counter + '.');

