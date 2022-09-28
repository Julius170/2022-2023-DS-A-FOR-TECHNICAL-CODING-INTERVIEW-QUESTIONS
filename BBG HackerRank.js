function minimumMoves(arr1: number[], arr2: number[]): number {
    
    let totalMoves = 0;
   
    for(let i = 0; i < arr1.length; i++){
        let currA = String(arr1[i])
        let currB = String(arr2[i])
       
        for(let j = 0; j < currA.length; j++){
            totalMoves += Math.abs(Number(currA[j]) - Number(currB[j]))
        }
    }
   
    return totalMoves
}






function counts(teamA: number[], teamB: number[]): number[] {

    teamA.sort((a,b) => a - b)


    let total = new Array(teamB.length);

    for(let b = 0; b < teamB.length; b++){
        let l = 0;
        let r = teamA.length - 1;
        let pos = 0;

    while(l <= r){
        let mid = Math.floor((l + r)/2) 
        
                    
        if(teamA[mid] > teamB[b]){
            r = mid - 1;
        }
        
        else {
            l = mid + 1   
            pos = mid + 1;         
        }

}