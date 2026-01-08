class Calculator {
    constructor(initialValue = 0) {
        this.value = initialValue;
    }

    add(value) {
        this.value += value;
        return this;
    }

    subtract(value) {
        this.value -= value;
        return this;
    }

    multiply(value) {
        this.value *= value;
        return this;
    }

    division(value) {
        if (value == 0) {
            console.log("Can't devide by zero!");
            return this;
        }
        this.value /= value;
        return this;
    }

    getResult() {
        return this.value;
    }
}

module.exports = { Calculator };
