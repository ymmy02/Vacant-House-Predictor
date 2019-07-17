<template>
    <div class="container" style="text-align:center;">
    <div>
        <b-card
            :img-src="imageUrl"
            img-alt="Image"
            img-top
            style="width:600px;"
            tag="article"
            class="mb-2"
        >
            <!-- style="max-width: 20rem;" -->
            <b-card-text>
            住宅の外観画像を送信してください。
            </b-card-text>

            <b-form-file 
                accept="image/*"
                :file-name-formatter="formatNames"
                @change="changeImage"></b-form-file>

            <b-button variant="outline-primary" @click="submitImage">送信</b-button>
            <div class="d-flex justify-content-center mb-3" v-if="loading">
                <b-spinner label="Loading..."></b-spinner>
            </div>
            <b-alert
                :show="showResult"
                dismissible
                :variant="alertType"
                @dismissed="showResult=false"
            >{{ resultMessage }}</b-alert>
        </b-card>
    </div>
    </div>
</template>

<script>
import noimage from "../assets/noimage.png";
import { apiUrl } from "../constants";
import axios from 'axios';

export default {
    data() {
        return {
            image: null,
            imageUrl: noimage,
            loading: false,
            showResult: false,
            resultMessage: '',
            alertType: ''
        }
    },
    methods: {
      formatNames(files) {
        return files[0].name
      },
      changeImage(e) {
        this.showResult = false,
        this.resultMessage = '';
        this.alertType = '';
        this.image = e.target.files[0];
        this.imageUrl = this.image ? URL.createObjectURL(this.image) : noimage;
      },
      submitImage(e) {
        this.loading = true;
        const formData = new FormData();
        formData.append('image', this.image)
        const config = {
            headers: {
                'content-type': 'multipart/form-data'
            }
        }
        console.log(apiUrl);
        axios.post(apiUrl, formData, config)
            .then(res => {
                const occupied = res.data.occupied;
                const vacant = res.data.vacant;
                console.log(`Occupied Parcentage: ${occupied}`);
                console.log(`Vacant Parcentage: ${vacant}`);

                this.judgeAndShowResult(occupied, vacant);
            })
            .catch(err => console.log(err))
            .finally(() => this.loading = false);
      },
      judgeAndShowResult(occupied, vacant) {
        if (occupied > vacant) {
            this.resultMessage = "空き家でないと判断されました。";
            this.alertType = 'info';
        } else {
            this.resultMessage = "空き家と判断されました。"
            this.alertType = 'danger';
        }
        this.showResult = true;
      }
    }
}
</script>

<style scoped>
</style>

