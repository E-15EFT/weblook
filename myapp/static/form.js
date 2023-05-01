
    let form = document.getElementById('form')

    let handleSubmit = async (e) => {
        e.preventDefault()
        let room = e.target.room.value.toUpperCase()

        let response = await fetch(`/get_token/?channel=${room}`)
        let data = await response.json()

        let UID = data.uid
        let token = data.token

        sessionStorage.setItem('UID', UID)
        sessionStorage.setItem('token', token)
        sessionStorage.setItem('room', room)

        window.open('/room', '_self')
    }
    form.addEventListener('submit', handleSubmit)
    document.getElementById('mic-btn').addEventListener('click', toggleMic)

