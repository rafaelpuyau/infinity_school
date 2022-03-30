const students = [
    {
      name: 'Rafael',
      age: 46,
    },
    {
      name: 'Luke',
      age: 65,
    },
    {
      name: 'Roger',
      age: 31,
    },
    {
      name: 'Axl',
      age: 51,
    },
    {
      name: 'Rodrigo',
      age: 29,
    }
  ];

  // Filter
  let filteredStudent = students.filter(student => student.name.includes('R'))
//   let filteredStudent = students.filter(student => student.name.includes('R')).map(nome => nome.name.toLowerCase())

  let filteredStudentByAge = students.filter(student => student.age > 50)

  console.log(filteredStudent)
  console.log('-- X --')
  console.log(filteredStudentByAge)

  // Reduce
  let somaIdades = students.reduce( (prevVal, currentAge) => prevVal + currentAge.age, 0)

  console.log(somaIdades)

  // Map
  currentYear = new Date().getFullYear()

  let anoNascimento = students.map( currentAge => currentYear - currentAge.age)

  console.log(anoNascimento)