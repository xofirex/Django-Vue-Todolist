<template>
  <div id="app">
    <div>

      <b-card

        style="max-width: 18rem;"
        class="mb-2"
      >
        <div class="bg-secondary">
          <div class="text-light">TODO list</div>
        </div>
        <div
          v-for="(task, index) in all_tasks"
          class="todo"
          style="display: flex"
        >
          <div class="task-element">
            <div v-if="task.is_complete">
              <b-icon icon="check-circle"
                      @click="update_task(task.id, task.is_complete, index)">
              </b-icon>
              <em>{{task.task_name}}</em>
            </div>
            <div v-if="!task.is_complete">
              <b-icon icon="circle"
                      @click="update_task(task.id, task.is_complete, index)"></b-icon>
              {{task.task_name}}
            </div>


          </div>
          <div class="delete-task">
            <b-icon @click="delete_task(task.id, index)" icon="bag-fill"></b-icon>
          </div>
        </div>
        <div class="add_task">
          <button class="btn" @click="add_task">➕</button>
          <input placeholder="Новая задача..." type="text" v-model="new_task.task_name">
        </div>

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
      delete_task: function (id, index) {
        const axios = require('axios');
        axios.delete('http://127.0.0.1:8000/api/tasks/' + id)
          .then(response => (this.all_tasks.splice(index, 1)));
      },
      update_task: function (id, is_complete, index) {
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
    get_task() {
      const axios = require('axios');
      axios
        .get('http://127.0.0.1:8000/api/tasks/')
        .then(response => (this.all_tasks = response.data));
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card-body {
    padding: 0;
  }

  .text-light {
    margin-left: 10px;
    text-align: left;
    color: #f8f9fa !important;
  }

  .bg-secondary {
    background-color: #6c757d !important;
    margin-bottom: 20px;
  }

  .add_task {
    margin-top: 100px;
  }

  .todo {
    margin-bottom: 5px;
    margin-left: 10px;
  }

  .task-element {
    position: absolute;
    margin-bottom: 5px;
  }

  .delete-task {
    margin-left: 90%;
  }
</style>
