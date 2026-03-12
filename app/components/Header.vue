<template>
    <UHeader title="Famiglia Sangue">

        <UNavigationMenu :items="items" />

        <template #right>
            <UButton
            v-if="!user_information.discord_id"
            :to="discord_auth"
            icon="ic:baseline-discord"
            class="bg-[#5865F2] text-[#E0E3FF] hover:bg-[#E0E3FF] hover:text-[#5865F2] active:bg-[#E0E3FF]"
            >
                Login
            </UButton>
            <UDropdownMenu
            :items="dropdownitems"
            v-else
            >
                <UButton
                variant="subtle"
                color="neutral"
                :avatar="{
                    src: user_information.discord_avatar_url,
                    loading: 'lazy'
                }"
                >
                    {{ user_information.discord_username }}
                </UButton>
            </UDropdownMenu>

        </template>
    </UHeader>
</template>

<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui';
import type UserInformation from '~/types/UserInformation';
import type { DropdownMenuItem } from '@nuxt/ui'


// varibles
const items = ref<NavigationMenuItem[]>([

])

const dropdownitems =ref<DropdownMenuItem[]>([
    {
        'label': 'Logout',
        icon: 'line-md:logout',
        onSelect(e) {
            localStorage.clear()
            user_information.value.discord_id = undefined
        },
    }
])

// injects
const discord_auth = inject("discord_auth")!
const user_information = inject<Ref<UserInformation>>("user_information")!


</script>