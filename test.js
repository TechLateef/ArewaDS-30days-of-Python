// function process(n, myList) {
//     let totalSum =0;
//     for (let i = 0; i < myList.length; i++) {
//       totalSum += myList[i];
//       console.log('myliat sum', myList[i]);
//     }
//     console.log('total sum', totalSum);
  
//     let remainder = 0
  
//     for (let i = 0; i < myList.length; i++) {
//       if (myList[i] % 2 == 0) {
//         totalSum -= myList[i];
//         console.log('my total when we subtract', totalSum)
//       } else {
//         totalSum += myList[i];
//         console.log('my total when we add', totalSum)

//       }
//     }
  
//     remainder = totalSum
//     if (remainder % 2 === 0) {
//       modifiedRemainder = remainder * 2;
//     } else {
//       modifiedRemainder = remainder * n;
//     }
  
//     return modifiedRemainder;
//   }
  
//   let output = process(3, [1, 2, 3]);
//   console.log(output);
  



function processList(n, myList) {
    // Calculate the sum of the list
    const totalSum = myList.reduce((accumulator, current) => accumulator + current, 0);
  
    // Create a copy of the original list to store the modified values
    const modifiedList = [...myList];
  
    // Iterate through the original list and modify the copied list
    for (let i = 0; i < myList.length; i++) {
      const num = myList[i];
  
      if (i % 2 === 0) { // Check if the number is even
        modifiedList[i] -= num;
      } else { // If the number is odd
        const remainder = num % n;
  
        if (remainder % 2 === 0) {
          modifiedList[i] = remainder * 2;
        } else {
          modifiedList[i] = remainder * n;
        }
      }
    }
  
    // Calculate the remainder using the modified list
    const remainder = modifiedList.reduce((accumulator, current) => accumulator + current, 0);
  
    // Return the modified list and the remainder
    return { modifiedList, remainder };
  }
    let output = processList(3, [1, 2, 3]);
  console.log(output);