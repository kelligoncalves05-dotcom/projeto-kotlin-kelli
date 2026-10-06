
// Projeto Kotlin - Kelli Gonçalves
// Desenvolvedora Android Jr | Em transição de carreira

data class Tarefa(val id: Int, val titulo: String, var concluida: Boolean = false)

fun main() {
    println("Olá! Eu sou a Kelli, Dev Android Kotlin! 🚀")
    
    val nome = "Kelli"
    val linguagem = "Kotlin"
    val foco = "Android"

    println("Nome: $nome | Linguagem: $linguagem | Foco: $foco")
    
    val minhasTarefas = mutableListOf(
        Tarefa(1, "Aprender Kotlin básico"),
        Tarefa(2, "Criar primeiro app Android"),
        Tarefa(3, "Subir projeto no GitHub", true)
    )

    mostrarTarefas(minhasTarefas)
    mostrarObjetivo()
}

fun mostrarTarefas(lista: List<Tarefa>) {
    println("\n--- Minhas Tarefas Dev ---")
    for (tarefa in lista) {
        val status = if (tarefa.concluida) "✅" else "⏳"
        println("$status ${tarefa.titulo}")
    }
}

fun mostrarObjetivo() {
    println("\nEm busca da primeira oportunidade como Dev Jr Android!")
    println("GitHub: github.com/kelligoncalves05")
}