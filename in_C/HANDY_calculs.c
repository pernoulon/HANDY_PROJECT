// Notre fichier calculs de HANDY depuis fichier textes

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct Struct_variables {
    double xc ;
    double xe ;
    double n ;
    double w ;
} ;
struct Struct_params {
    double am ;
    double aM ;
    double bc ;
    double be ;
    double g ;
    double l ;
    double s ;
    double d ;
    double k ;
    double r ;
} ;

void readFile(const char * FileName, struct Struct_variables * variables, struct Struct_params * params, int size) {
/* This function reads a text file of our initial conditions : 4 variables and 10 parameters.
It stocks the values in the two structures corresponding to the two types of arguments
(variables and parameters). */ 

    FILE * file = fopen(FileName, "r");
    if (file == NULL) printf("Error: file does not exist");

    int n = 0;
    double val;
    char line[100];
    while (fgets(line, 100, file) != NULL) {

        char * espace = strchr(line,' ') ;
        val = atof(espace) ; 

        if (n == 0) variables->xc = val ;
        if (n == 1) variables->xe = val ;
        if (n == 2) variables->n = val ;
        if (n == 3) variables->w = val ; 

        if (n == 4) params->am = val ;
        if (n == 5) params->aM = val ;
        if (n == 6) params->bc = val ;
        if (n == 7) params->be = val ;
        if (n == 8) params->g = val ;
        if (n == 9) params->l = val ;
        if (n == 10) params->s = val ;
        if (n == 11) params->d = val ;
        if (n == 12) params->k = val ;
        if (n == 13) params->r = val ;

        n = n + 1 ;
        
        if (n>size) break ;
    }
    fclose(file);
}

void paramsDefault(struct Struct_params * params) {
    params->am = 0.01 ;
    params->aM = 0.07 ;
    params->bc = 0.03 ;
    params->be = 0.03 ;
    params->g = 0.01 ;
    params->l = 100 ;
    params->s = 0.0005 ;
    params->d = 0.00000667 ;
    params->k = 0 ;
    params->r = 0.005 ;
}

void euler(struct Struct_variables * variables, struct Struct_params * params, int i) {
/* This function calculates the new four variables from the variables just before.
Incremeting with differential functions defined in the paper, using Euler method.*/

    // giving name for variables to make the program lighter
    double xc_prev = variables[i].xc ;
    double xe_prev = variables[i].xe ;
    double n_prev = variables[i].n ;
    double w_prev = variables[i].w ;

    double am = params->am ;
    double aM = params->aM ;
    double bc = params->bc ;
    double be = params->be ;
    double g = params->g ;
    double l = params->l ;
    double s = params->s ;
    double d = params->d ;
    double k = params->k ;
    double r = params->r ;

    //why
    double wth = (r * xc_prev) + (k * r * xe_prev) ; //dépend du temps
    double cc ;
    double ce ;
    double ac ;
    double ae ;

    if (wth != 0) {
        cc = fmin(1, w_prev/wth) * s * xc_prev ;
        ce = fmin(1, w_prev/wth) * k * s * xe_prev ;
    }
    else {
        cc = s * xc_prev ;
        ce = k * s * xe_prev ;
    }
    if (s * xc_prev != 0) {
        ac = am + (fmax(0, 1 - (cc / (s * xc_prev))) * (aM - am)) ;
    }
    else {
        ac = am ;
    } 
    if (s * xe_prev != 0) {
        ae = am + (fmax(0, 1 - (ce / (s * xe_prev))) * (aM - am)) ;
    }
    else {
        ae = am ;
    }

    // why
    double dxc = (bc * xc_prev) - (ac * xc_prev) ;
    double dxe = (be * xe_prev) - (ae * xe_prev) ;
    double dn = (g * n_prev * (l - n_prev)) - (d * xc_prev * n_prev) ;
    double dw = (d * xc_prev * n_prev) - cc - ce ;

    double xc_next = xc_prev + dxc ;
    if (xc_next < 0) xc_next = 0 ;
    double xe_next = xe_prev + dxe ;
    if (xe_next < 0) xe_next = 0 ;
    double n_next = n_prev + dn ;
    if (n_next < 0) n_next = 0 ;
    double w_next = w_prev + dw ;
    if (w_next < 0) w_next = 0 ;

    // Addition of values of structure n°i+1
    variables[i+1].xc = xc_next ;
    variables[i+1].xe = xe_next ;
    variables[i+1].n = n_next ;
    variables[i+1].w = w_next ;
}

double findMax(struct Struct_variables * variables, char variable_name, int t) {
/* This function finds the maximum value for each of our 4 variable. It is then used
for the normalisation. */ 

    if (variable_name == 'c') {
        double mx = 0 ;
        for (int i = 0; i < t; i++) {
            double val = variables[i].xc ;
            mx = fmax(mx, val);
        }
        return mx ;
    }
    if (variable_name == 'e') {
        double mx = 0 ;
        for (int i = 0; i < t; i++) {
            double val = variables[i].xe ;
            mx = fmax(mx, val);
        }
        return mx ;
    }

    if (variable_name == 'n') {
        double mx = 0 ;
        for (int i = 0; i < t; i++) {
            double val = variables[i].n ;
            mx = fmax(mx, val);
        }
        return mx ;
    }

    if (variable_name == 'w') {
        double mx = 0 ;
        for (int i = 0; i < t; i++) {
            double val = variables[i].w ;
            mx = fmax(mx, val);
        }
        return mx ;
    }
    return 0 ;
}

void runAuto(struct Struct_variables * variables, struct Struct_params * params, int t) {
/* This function fulfills our tab_variables following the time using our
euleur function and normalizes each value. */

    for (int i = 0 ; i < t-1 ; i++) {
        euler(variables, params, i) ;
    }

    //normalisation
    double mx_XC = findMax(variables, 'c', t) ; 
    double mx_XE = findMax(variables, 'e', t) ;
    double mx_N = findMax(variables, 'n', t) ;
    double mx_W = findMax(variables, 'w', t) ;

    for (int i = 0 ; i < t ; i++) {
        if (mx_XC == 0) variables[i].xc = 0 ;
        else variables[i].xc = (variables[i].xc / mx_XC) ;
        if (mx_XE == 0) variables[i].xe = 0 ;
        else variables[i].xe = (variables[i].xe / mx_XE) ;
        if (mx_N == 0) variables[i].n = 0 ;
        else variables[i].n = (variables[i].n / mx_N) ;
        if (mx_W == 0) variables[i].w = 0 ;
        else variables[i].w = (variables[i].w / mx_W) ;
    }
}

void finalFile(char * FileName, struct Struct_variables * variables, struct Struct_params * params, int t) {
/* This function creates the final file containing all datas to send to python
(one variable per column). */
;

    FILE * file = fopen(FileName, "w");
    if (file == NULL) printf("Error: can not open file.\n");

    fprintf(file, "%s, %f, %f, %f, %f\n%s, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f\n", "Variables at t=0", variables->xc, variables->xe, variables->n, variables->w, "Parameters", params->am, params->aM, params->bc, params->be, params->g, params->l, params->s, params->d, params->k, params->r);

    for (int i=0 ; i<t ; i++) {  // line break implemented for each i 
        fprintf(file, "%f, %f, %f, %f\n", variables[i].xc, variables[i].xe, variables[i].n, variables[i].w);
    } // Warning : frpintf writes strings and not doubles into the file -> Need to convert in python file 

    fclose(file);
}

int main(int argc, char const *argv[]) {
/* This is our main function. It reads a text file.
Then calculates datas. Creates a final file to send the datas to Python. */
;
    // system("ls") ;

    int t = 1000;
    struct Struct_variables tab_variables[t] ;// = tableau de t structures de types struct_vari
    struct Struct_params parameters ; //1 seule car les variables ne changent pas
    int size = 13; //taille des params (j'ai enlevé le temps à la fin)

    const char * condition = argv[1] ;
    
    char * s = "s" ;
    if (strcmp(condition, s) == 0) {
        const char * file_path = argv[2] ;
        readFile(file_path, tab_variables, &parameters, 15);
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_scenario.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/interface.py --fileName results_python_scenario.txt") ;
    }

    char * f = "f" ;
    if (strcmp(condition, f) == 0) {
        const char * file_path = argv[2] ;
        readFile(file_path, tab_variables, &parameters, 15);
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_file.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/interface.py --fileName results_python_file.txt") ;
    }
    char * c = "c" ;
    if (strcmp(condition, c) == 0) {
        double xc_0 = atof(argv[2]) ;
        printf("%f\n", xc_0) ;
        tab_variables[0].xc = xc_0 ;
        double xe_0 = atof(argv[3]) ;
        tab_variables[0].xe = xe_0 ;
        double n_0 = atof(argv[4]) ;
        tab_variables[0].n = n_0 ;
        double w_0 = atof(argv[5]) ;
        tab_variables[0].w = w_0 ;
        paramsDefault(&parameters) ;
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_cursors.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/interface.py --fileName results_python_cursors.txt") ;
    }

    
    
    return 0;
}





// anciens fichiers textes
// template pyhton pour définir fonction