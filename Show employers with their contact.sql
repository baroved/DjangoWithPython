use djangoDB;
select smarti_employer.name as 'employerName',
smarti_contact.firstName as 'contactFirstName',
smarti_contact.lastName as 'contactLastName',
smarti_contact.phone as 'contactPhone',
smarti_contact.email as 'contactEmail'
from smarti_contact
inner join smarti_employer
 on smarti_contact.employerId_id=smarti_employer.id
 order by smarti_employer.name