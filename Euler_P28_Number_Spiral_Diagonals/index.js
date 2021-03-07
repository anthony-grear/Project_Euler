// var diagonalArray = [1]; var initialValue = 1;
// var commonDifference = 2; var differenceCounter = 0;
// var x....groupCounter = 1;
function sum (array) {
  return array.reduce((a,b) => a+b,0);
}
var diagonalArray = [1];
var initialValue = 1;
var commonDifference=0
for (groupCounter=1;groupCounter<=500;groupCounter++){
  commonDifference+=2;
  for (diffCount=1;diffCount<=4;diffCount++) {
    initialValue+=commonDifference;
    diagonalArray.push(initialValue);
  }
}

console.log(sum(diagonalArray))
