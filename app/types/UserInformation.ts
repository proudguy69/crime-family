export default interface UserInformation {
    discord_id: number|undefined
    discord_username: string|undefined
    discord_avatar_url: string|undefined

    roblox_id: number|undefined|null
    roblox_username: string|undefined|null
    roblox_avatar_url: string|undefined|null

    web_token: string
}