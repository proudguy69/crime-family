<template>
    <UPageSection>
        <UPageCard variant="subtle">
            <UForm>
                <UFormField label="First Name">
                    <UInput />
                </UFormField>

                <UFormField label="Middle Name">
                    <UInput />
                </UFormField>

                <UFormField label="Last Name">
                    <UInput />
                </UFormField>

                <UFormField label="Date of Birth">
                    <UInputDate />
                </UFormField>

                <UFormField label="Rank">
                    <USelect :items="ranks" v-model="selected_rank"/>
                </UFormField>
                
                    
            </UForm>
        </UPageCard>
    </UPageSection>
</template>

<script setup lang="ts">

const ranks = ref([
    "Caporegime",
    "Sgarrista",
    "Picciotto di guardia",
    "Soldato",
    "Picciotto",
    "Enforcer"
])

const selected_rank = ref("Enforcer")

</script>