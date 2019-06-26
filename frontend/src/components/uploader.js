import React, { Component } from 'react';
import axios, { post } from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

export default class Uploader extends Component {
    constructor(props) {
        super(props);
        this.state = {
            file: null,
            result: '',
        }

        this.onSubmit = this.onSubmit.bind(this);
        this.onChange = this.onChange.bind(this);
    }

    onSubmit(e) {
        e.preventDefault();
        this.uploadFile(this.state.file).then((res) => {
            console.log(res.data);
        })
    }

    uploadFile(file) {
        const url = 'http://localhost:8000/api/';
        const formData = new FormData();
        formData.append('image',file)
        const config = {
            headers: {
                'content-type': 'multipart/form-data'
            }
        }
        return  post(url, formData, config)
    }

    onChange(e) {
        this.setState({
            file   : e.target.files[0],
            fileUrl: URL.createObjectURL(e.target.files[0]),
            result : ''
        });
    }

    render() {
        return (
            <div>
                <div className="upload">
                    <form onSubmit={this.onSubmit}>
                        <input type="file" 
                            accept="image/*"
                            onChange={this.onChange}/>
                        <input type="submit"
                            className="btn btn-primary" 
                            value="送信"/>
                    </form>
                    <div className="preview">
                        <img src={this.state.fileUrl} />
                    </div>
                </div>
                <div className="result">{this.state.result}</div>
            </div>
        )
    }
}