<template>
  <UApp>
    <Header />
    <NuxtPage />
  </UApp>
</template>

<script setup>
import Header from './components/Header.vue';
import discordAuthenticate from './utils/authenticate';
//import UserInformation from './types/UserInformation';

// varibles
const discord_auth_uri = {
  dev: 'https://discord.com/oauth2/authorize?client_id=1481263551795695676&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fauthorize%2Fdiscord&scope=identify',
  prod: ''
}.dev

const api_uri = {
  dev: 'http://localhost:8000',
  prod: ''
}.dev

const roblox_auth_uri = {
  dev: 'https://apis.roblox.com/oauth/v1/authorize?client_id=2359556374392113378&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fauthorize%2Froblox&scope=openid%20profile&response_type=code',
  prod: ''
}.dev


// refs
const user_information = ref({
})


// provides
console.log(api_uri)
provide('discord_auth', discord_auth_uri)
provide('roblox_auth', roblox_auth_uri)
provide('user_information', user_information)
provide('api_uri', api_uri)

// functions

// methods
onMounted(async () => {
  const web_token = localStorage.getItem('web_token')
  if (!web_token) {return}
  await discordAuthenticate(web_token, user_information)
})

</script>