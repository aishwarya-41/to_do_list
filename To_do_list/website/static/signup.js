function lightDark()
{
    const lD = document.querySelector("#s1").value
    if (lD==="light")
    {
        document.querySelector("body").style.backgroundImage = "radial-gradient(rgb(185, 227, 227),white)"
        document.querySelector("#d1").style.backgroundColor = "white"
        document.querySelectorAll(".d2").forEach(el => {
                el.style.backgroundColor = "white"
                })

        document.querySelectorAll(".i1").forEach(el => {
                el.style.backgroundColor = "white"
                el.style.border ="2px solid rgb(94, 106, 122)"
                el.style.color ="black"
                })

        document.querySelector("#d3").style.backgroundColor = "white"
        document.querySelector("p").style.color = "black"
        document.querySelector("a").style.color = "purple"
    }
    else if (lD==="dark")
    {
        document.querySelector("body").style.backgroundImage = "radial-gradient(rgb(38, 124, 124),grey)"
        document.querySelector("#d1").style.backgroundColor = "#2d3436"
        document.querySelectorAll(".d2").forEach(el => {
                el.style.backgroundColor = "#2d3436"
                })

        document.querySelectorAll(".i1").forEach(el => {
                el.style.backgroundColor = "rgb(47, 54, 64)"
                el.style.border ="2px solid rgb(94, 106, 122)"
                el.style.color ="white"
                })

        document.querySelector("#d3").style.backgroundColor = "#2d3436"
        document.querySelector("p").style.color = "white"
        document.querySelector("a").style.color = "white"

    }
}