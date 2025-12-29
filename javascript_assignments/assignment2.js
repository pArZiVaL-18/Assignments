const num1 = 20;
const num2 = 0;

console.log("Addition of numbers : ", num1 + num1);
console.log("Subtraction of numbers : ", num1 - num1);
console.log("Multiplication of numbers : ", num1 * num1);
console.log(
    "Division of num1 by num2",
    num2 != 0 ? num1 / num2 : " Not possible!"
);

if (num2 != 0) {
    if (num1 / num2 > 10) {
        console.log("The result of the division is greater than 10.");
    } else {
        console.log("The result of the division is less than 10.");
    }
} else {
    console.log("Division is not possible. ");
}
