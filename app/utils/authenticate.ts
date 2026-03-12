import type User from "~/types/User"
import type UserInformation from "~/types/UserInformation"

interface Response {
    success: boolean
    message: string|undefined
    user: User|undefined
}

async function discordAuthenticate(web_token:string, user_information:Ref<UserInformation>) {
    const response = await fetch('http://localhost:8000/authenticate', {headers: {'Authorization': web_token}})
    const data = await response.json() as Response
    user_information.value.discord_id = data.user?.discord_id!
    user_information.value.discord_username = data.user?.discord_username!
    user_information.value.discord_avatar_url = data.user?.discord_avatar_url!
    user_information.value.web_token = web_token

    console.log(data.user)

    user_information.value.roblox_id = data.user?.roblox_id
    user_information.value.roblox_username = data.user?.roblox_username
    user_information.value.roblox_avatar_url = data.user?.roblox_avatar_url
}

export default discordAuthenticate