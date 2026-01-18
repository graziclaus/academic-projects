document.querySelectorAll('.open-popup').forEach(button => 
{

    button.addEventListener('click', () => 
        {

        const popupId = button.getAttribute('data-popup');
        document.getElementById(popupId).classList.add('show');

    });
});

document.querySelectorAll('.popup-close').forEach(closeBtn => 
{

    closeBtn.addEventListener('click', () => 
    {

        const popupId = closeBtn.getAttribute('data-popup');
        document.getElementById(popupId).classList.remove('show');

    });
});

document.querySelectorAll('.popup-overlay').forEach(popup =>
{
    popup.addEventListener('click', (e) => 
    {

        if(e.target === popup)
        {

            popup.classList.remove('show');
            
        }
    });
});
