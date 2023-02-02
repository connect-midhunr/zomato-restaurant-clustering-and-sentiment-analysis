function ChangeButtonColor()
{
    document.getElementById('submit-button').style.backgroundColor = '#272c48';
}

function RevertButtonColor()
{
    document.getElementById('submit-button').style.backgroundColor = '#ff7428';
}

function ClearDefaultText()
{
    document.getElementById('text-input').value = '';
}

function SiteLoading() 
{
    ClearDefaultText();
}

window.onload = SiteLoading();