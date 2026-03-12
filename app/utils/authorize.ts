import type User from "~/types/User"
import type UserInformation from "~/types/UserInformation"

interface Response {
    success: boolean
    message: string|undefined
    user: User|undefined
    web_token: string|undefined
}

async function authorizeDiscord(code:string, api_uri:string, user_information:Ref<UserInformation>) {
    console.log(api_uri)
    const response = await fetch(`http://localhost:8000/authorize/discord?code=${code}`)
    const data:Response = await response.json()
    if (!data.success) {
        return data.message
    }
    localStorage.setItem('web_token', data.web_token!)
    user_information.value.discord_id = data.user?.discord_id!
    user_information.value.discord_username = data.user?.discord_username!
    user_information.value.discord_avatar_url = data.user?.discord_avatar_url!
    user_information.value.web_token = data.web_token!
    return
}

async function authorizeRoblox(code:string) {
    
}

export {authorizeDiscord, authorizeRoblox}