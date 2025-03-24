
select eu.unique_id, e.name from Employees as e Left Outer Join EmployeeUNI as eu on
e.id = eu.id 