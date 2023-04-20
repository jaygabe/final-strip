


export const PushNote = () => {

    const sendNote = () => {
        console.log("sending notification")
        Notification.requestPermission().then(perm => {
            console.log(perm)
            if (perm == "granted") {
                new Notification("Example Notification", {  // this is not showing in the chrome browser for some reason
                    body: "This is more text",
                })
                
            }
        })
    }

    return (
        <button onClick={sendNote}>Click me!</button>
    )
}