<template>
  <div id="app">
    <div>
      <b-card
        title="Список задач"
        style="max-width: 20rem;"
        class="mb-2"
      >
        <b-card-text style="text-align: left">
          <div
            v-for="(task, index) in all_tasks"
            class="todo"
            style="display: flex"
          >
            <div>
              <b-icon v-if="task.is_complete" icon="check-circle"
                      @click="updateTask(task.id, task.is_complete, index)"></b-icon>
              <b-icon v-if="!task.is_complete" icon="circle"
                      @click="updateTask(task.id, task.is_complete, index)"></b-icon>
              {{ task.task_name }}
            </div>
            <div>
              <button @click="deleteData(task.id, index)">
                <b-icon icon="bag-fill"></b-icon>
              </button>
            </div>
          </div>
          <div class="add_task">
            <button class="add_task btn" @click="add_task">➕</button>
            <input placeholder="Новая задача..." type="text" v-model="new_task.task_name">
          </div>
        </b-card-text>
      </b-card>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Todo',
    data() {
      return {
        new_task: {
          task_name: '',
          is_complete: false
        },
        all_tasks: [],
      }
    },
    methods: {
      add_task() {
        if (this.new_task.task_name != '') {
          const axios = require('axios');
          axios.post('http://127.0.0.1:8000/api/tasks/', this.new_task)
            .then(({data}) => (this.all_tasks.push(data),
              this.new_task.task_name = ''))
        }
      },
      deleteData: function (id, index) {
        const axios = require('axios');
        axios.delete('http://127.0.0.1:8000/api/tasks/' + id)
          .then(response => (this.all_tasks.splice(index, 1)));
      },
      updateTask: function (id, is_complete, index) {
        const status = is_complete ? false : true;
        const axios = require('axios');
        const str = {
          is_complete: status
        };
        axios.put(`http://127.0.0.1:8000/api/tasks/${id}/`, str)
          .then(({data}) => {
            console.log(data)
            this.all_tasks.splice(index, 1, data)
            console.log(this.all_tasks)
            console.log(index)
          });
      },

    },
    mounted() {
      const axios = require('axios');
      axios
        .get('http://127.0.0.1:8000/api/tasks/')
        .then(response => (this.all_tasks = response.data));
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
