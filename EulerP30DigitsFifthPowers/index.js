for (let i=150000;i<200000;i++) {
  let stringNumber = i.toString();
  let stringList = stringNumber.split("");
  let numberList = stringList.map((x)=> parseInt(x));
  let power5List = numberList.map((x)=>x**5);
  let sumPowers = power5List.reduce((a,b)=>a+b)
  if (sumPowers===i) {
    console.log(i + " True");
    break;
  }
  console.log();
  
  console.log(i+": sum of digits to power 5 -->"+ sumPowers);
}
//4150,4151, 54748, 92727, 93084, 194979  