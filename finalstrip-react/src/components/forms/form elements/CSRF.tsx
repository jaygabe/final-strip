
export const CSRF = () => {
    
    // gets csrf token from cookie
    function getToken(name:string){
        var cookieValue = 'cookie not found'
        if (document.cookie && document.cookie !== ''){
                var cookies = document.cookie.split(';')
                for (var i =0; i < cookies.length; i++){
                    var cookie = cookies[i].trim()
                    if (cookie.substring(0, name.length +1) === (name + '=')){
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                        break
                    }
                }
        }
        return cookieValue
    }
    
    return <input type="hidden" value={getToken("csrftoken")} name="csrfmiddlewaretoken" />
}
