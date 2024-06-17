// today's temperature in kelvin degrees
let kelvin = 293;

kelvin = 0;
// converting kelvin to celsius
let celsius = kelvin - 273;

console.log(`The temperature is ${celsius} degrees Celsius.`);

// converting celsius to fahrenheit
let fahrenheit = celsius * (9/5) + 32;

// rounding fahrenheit
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

//converting celsius to newton
let newton = celsius * (33/100);

// rounding newton
newton = Math.floor(newton);

console.log(`The temperature is ${newton} degrees Newton.`)