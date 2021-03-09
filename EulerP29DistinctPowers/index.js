let powersArray = []
for (let i=2;i<101;i++) {
  for (let j=2;j<101;j++) {
    powersArray.push(i**j);
    
  }
}
mySet=new Set(powersArray.sort(function(a,b){return a-b;}));

console.log(mySet.size);