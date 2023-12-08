//Beats 100.00%of users with C

typedef struct {
    // User defined data may be declared here.
    pthread_mutex_t mutex; 
    pthread_cond_t cond[2];
    int status;

} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    // Initialize user defined data here.
    pthread_mutex_init(&obj->mutex, NULL);
    pthread_cond_init(&obj->cond[0], NULL);
    pthread_cond_init(&obj->cond[1], NULL);
    obj->status = -1;

    return obj;
}

void first(Foo* obj) {
    
    // printFirst() outputs "first". Do not change or remove this line.
    pthread_mutex_lock(&(obj->mutex)); 
    
    printFirst();
    
    obj->status = 10;
    pthread_cond_signal(&obj->cond[0]);
    pthread_mutex_unlock(&(obj->mutex)); 

}

void second(Foo* obj) {
    
    // printSecond() outputs "second". Do not change or remove this line.
    pthread_mutex_lock(&obj->mutex); 
    while(obj->status != 10){
        pthread_cond_wait(&obj->cond[0], &obj->mutex); 
    }
    printSecond();
    obj->status = 100;
    pthread_cond_signal(&obj->cond[1]);
    pthread_mutex_unlock(&obj->mutex); 

}

void third(Foo* obj) {
    
    // printThird() outputs "third". Do not change or remove this line.
    pthread_mutex_lock(&obj->mutex); 
    while(obj->status != 100){
        pthread_cond_wait(&obj->cond[1], &obj->mutex); 
    }
    printThird();
    pthread_mutex_unlock(&obj->mutex); 
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    /* fasrter runtime without this, but i think its good practice to include
    pthread_mutex_destroy(&obj->mutex);
    pthread_cond_destroy(&obj->cond[0]);
    pthread_cond_destroy(&obj->cond[1]);
    
    */
    free(obj);
}
