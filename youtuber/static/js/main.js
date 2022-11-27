let showDates = document.getElementsByClassName('show-date')
let statusDisplay = document.getElementsByClassName('status-d')
let button = document.getElementsByClassName('btn-primary')
let button_cancel = document.getElementsByClassName('btn-danger')

for(let i = 0 ; button.length > i ; i++){

    button[i].addEventListener('click', (e)=>{
        
        targetI =e.target.dataset.info
        let date = new Date()
        let downloadDate = `${date.getFullYear()}-${date.getMonth()}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
        showDates[targetI-1].innerHTML = downloadDate
        statusDisplay[targetI-1].innerHTML = 'Inprogress...!'
        button[targetI-1].classList.add('disabled')
        button_cancel[targetI-1].classList.add('disabled')
        
    
    })
}    

for(let i = 0 ; button_cancel.length > i ; i++){
    button_cancel[i].addEventListener('click', (e)=>{
        targetI =e.target.dataset.info
        showDates[targetI-1].innerHTML = ' '
        statusDisplay[targetI-1].innerHTML = 'Deleted!'
     
    
    })
}    
